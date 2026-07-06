const dropZone = document.getElementById("dropZone");
const fileInput = document.getElementById("fileInput");
const preview = document.getElementById("preview");

dropZone.addEventListener("click", () => fileInput.click());

dropZone.addEventListener("dragover", (e) => {
  e.preventDefault();
  dropZone.classList.add("dragover");
});

dropZone.addEventListener("dragleave", () => {
  dropZone.classList.remove("dragover");
});

dropZone.addEventListener("drop", (e) => {
  e.preventDefault();
  dropZone.classList.remove("dragover");

  const file = e.dataTransfer.files[0];
  if (file) {
    fileInput.files = e.dataTransfer.files;
    showPreview(file);
  }
});

fileInput.addEventListener("change", () => {
  if (fileInput.files[0]) {
    showPreview(fileInput.files[0]);
  }
});

const dropText = document.getElementById("dropText");

function showPreview(file) {
  if (!file.type.startsWith("image/")) {
    alert("Please select an image.");
    return;
  }

  const reader = new FileReader();

  reader.onload = function (e) {
    preview.src = e.target.result;
    preview.style.display = "block";
    dropText.style.display = "none";
  };

  reader.readAsDataURL(file);
}

document.getElementById("uploadForm").addEventListener("submit", function (e) {
  if (fileInput.files.length === 0) {
    e.preventDefault();
    alert("You have not selected a picture!");
  }
});
