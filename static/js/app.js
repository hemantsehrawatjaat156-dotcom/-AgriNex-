/**
 * Kisan Crop Doctor - Frontend Controller
 */

document.addEventListener("DOMContentLoaded", () => {
  // Elements
  const samplesContainer = document.getElementById("samplesContainer");
  const dropArea = document.getElementById("dropArea");
  const fileInput = document.getElementById("fileInput");
  const dropIdle = document.getElementById("dropIdle");
  const dropPreview = document.getElementById("dropPreview");
  const previewImg = document.getElementById("previewImg");
  const clearBtn = document.getElementById("clearBtn");
  const uploadForm = document.getElementById("uploadForm");
  const analyzeBtn = document.getElementById("analyzeBtn");

  // Results elements
  const resultStatus = document.getElementById("resultStatus");
  const emptyState = document.getElementById("emptyState");
  const diagnosisWrapper = document.getElementById("diagnosisWrapper");
  const diagCrop = document.getElementById("diagCrop");
  const diagName = document.getElementById("diagName");
  const diagSci = document.getElementById("diagSci");
  const diagCategory = document.getElementById("diagCategory");
  const diagSeverity = document.getElementById("diagSeverity");
  const diagConf = document.getElementById("diagConf");
  const diagDesc = document.getElementById("diagDesc");
  const diagSymptoms = document.getElementById("diagSymptoms");
  const organicList = document.getElementById("organicList");
  const chemicalList = document.getElementById("chemicalList");
  const farmList = document.getElementById("farmList");

  // Solution tabs
  const solTabs = document.querySelectorAll(".sol-tab");
  const solPanes = document.querySelectorAll(".sol-pane");

  let currentFile = null;
  let currentSampleName = null;

  function removeHindi(value) {
    return String(value)
      .replace(/\s*\([^)]*[\u0900-\u097F][^)]*\)/g, "")
      .replace(/[\u0900-\u097F]+/g, "")
      .replace(/\s*[/,]\s*(?=[.,;:!?]|$)/g, "")
      .replace(/\s+([,.;:!?])/g, "$1")
      .replace(/\s{2,}/g, " ")
      .trim();
  }

  // 1. Solution Tab Navigation
  solTabs.forEach(tab => {
    tab.addEventListener("click", () => {
      solTabs.forEach(t => t.classList.remove("active"));
      solPanes.forEach(p => p.classList.remove("active"));

      tab.classList.add("active");
      const target = document.getElementById(tab.getAttribute("data-target"));
      if (target) target.classList.add("active");
    });
  });

  // 2. Load Preset Samples
  async function loadSamples() {
    try {
      const res = await fetch("/api/samples");
      const data = await res.json();
      if (data.success && data.samples) {
        samplesContainer.innerHTML = "";
        data.samples.forEach(sample => {
          const chip = document.createElement("button");
          chip.type = "button";
          chip.className = "sample-chip";
          const icon = document.createElement("i");
          icon.className = "fa-solid fa-leaf";
          chip.append(icon, document.createTextNode(` ${removeHindi(sample.name)}`));
          chip.title = removeHindi(sample.description);
          chip.addEventListener("click", () => selectSample(sample, chip));
          samplesContainer.appendChild(chip);
        });
      }
    } catch (err) {
      console.error("Failed to load samples:", err);
    }
  }

  function selectSample(sample, chipElement) {
    document.querySelectorAll(".sample-chip").forEach(c => c.classList.remove("active"));
    if (chipElement) chipElement.classList.add("active");

    currentSampleName = sample.filename;
    currentFile = null;

    previewImg.src = `/sample/${sample.filename}`;
    dropIdle.style.display = "none";
    dropPreview.style.display = "block";
  }

  // 3. Drag and Drop Handling
  dropArea.addEventListener("click", () => {
    if (!currentFile && !currentSampleName) fileInput.click();
  });

  dropArea.addEventListener("dragover", (e) => {
    e.preventDefault();
    dropArea.classList.add("dragover");
  });

  dropArea.addEventListener("dragleave", () => {
    dropArea.classList.remove("dragover");
  });

  dropArea.addEventListener("drop", (e) => {
    e.preventDefault();
    dropArea.classList.remove("dragover");
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      handleFile(e.dataTransfer.files[0]);
    }
  });

  fileInput.addEventListener("change", (e) => {
    if (e.target.files && e.target.files[0]) {
      handleFile(e.target.files[0]);
    }
  });

  function handleFile(file) {
    currentFile = file;
    currentSampleName = null;
    document.querySelectorAll(".sample-chip").forEach(c => c.classList.remove("active"));

    const reader = new FileReader();
    reader.onload = (event) => {
      previewImg.src = event.target.result;
      dropIdle.style.display = "none";
      dropPreview.style.display = "block";
    };
    reader.readAsDataURL(file);
  }

  clearBtn.addEventListener("click", (e) => {
    e.stopPropagation();
    currentFile = null;
    currentSampleName = null;
    fileInput.value = "";
    previewImg.src = "";
    dropPreview.style.display = "none";
    dropIdle.style.display = "block";
    document.querySelectorAll(".sample-chip").forEach(c => c.classList.remove("active"));
  });

  // 4. Form Submit & Disease Detection
  uploadForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    if (!currentFile && !currentSampleName) {
      alert("Please upload a crop image or select a sample.");
      return;
    }

    analyzeBtn.disabled = true;
    analyzeBtn.innerHTML = `<i class="fa-solid fa-spinner fa-spin"></i> Analyzing Crop Health...`;
    resultStatus.textContent = "Diagnosing...";
    resultStatus.className = "status-pill";

    try {
      const formData = new FormData();
      if (currentFile) {
        formData.append("image", currentFile);
      } else if (currentSampleName) {
        formData.append("sample_name", currentSampleName);
      }

      const res = await fetch("/api/predict", {
        method: "POST",
        body: formData
      });

      const resJson = await res.json();
      if (!resJson.success) {
        throw new Error(resJson.error || "Analysis failed.");
      }

      renderDiagnosis(resJson.data);

    } catch (err) {
      alert("Error: " + err.message);
      resultStatus.textContent = "Error";
    } finally {
      analyzeBtn.disabled = false;
      analyzeBtn.innerHTML = `<i class="fa-solid fa-magnifying-glass"></i> Detect Disease & Get Solutions`;
    }
  });

  // 5. Render Diagnosis and Remedies
  function renderDiagnosis(data) {
    emptyState.style.display = "none";
    diagnosisWrapper.style.display = "block";

    resultStatus.textContent = "Prescription Ready";
    resultStatus.className = "status-pill";

    diagCrop.textContent = removeHindi(data.crop_name);
    diagName.textContent = removeHindi(data.condition_name);
    diagSci.textContent = removeHindi(data.scientific_name);
    diagConf.textContent = `${data.confidence_percent}%`;

    // Category and Severity
    diagCategory.textContent = removeHindi(data.category);
    diagCategory.className = "badge badge-info";

    diagSeverity.textContent = `Severity: ${removeHindi(data.severity)}`;
    diagSeverity.className = `badge badge-${data.severity_color}`;

    // Description & Symptoms
    diagDesc.textContent = removeHindi(data.description);
    
    diagSymptoms.innerHTML = "";
    (data.symptoms || []).forEach(sym => {
      const li = document.createElement("li");
      li.textContent = removeHindi(sym);
      diagSymptoms.appendChild(li);
    });

    // Solutions
    renderTreatmentList(organicList, data.organic_remedies);
    renderTreatmentList(chemicalList, data.chemical_remedies);
    renderTreatmentList(farmList, data.farm_management);

    // Scroll to results on mobile
    if (window.innerWidth < 960) {
      diagnosisWrapper.scrollIntoView({ behavior: "smooth" });
    }
  }

  function renderTreatmentList(targetElement, items) {
    targetElement.innerHTML = "";
    (items || []).forEach(item => {
      const li = document.createElement("li");
      li.innerHTML = removeHindi(item);
      targetElement.appendChild(li);
    });
  }

  // Initial call
  loadSamples();
});
