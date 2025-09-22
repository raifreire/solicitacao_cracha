document.addEventListener('DOMContentLoaded', () => {
    const photoUpload = document.getElementById('photo-upload');
    const photoPreview = document.getElementById('photo-preview');
    const cropModal = document.getElementById('crop-modal');
    const imageToCrop = document.getElementById('image-to-crop');
    const applyCropBtn = document.getElementById('apply-crop');
    const cancelCropBtn = document.getElementById('cancel-crop');
    
    let cropper;

    photoUpload.addEventListener('change', (event) => {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = (e) => {
                imageToCrop.src = e.target.result;
                cropModal.style.display = 'block';
                if (cropper) {
                    cropper.destroy();
                }
                cropper = new Cropper(imageToCrop, {
                    aspectRatio: 1, // Proporção 1:1 para foto de crachá
                    viewMode: 1,
                    autoCropArea: 0.8,
                    zoomable: true,
                    background: false,
                    scalable: true,
                });
            };
            reader.readAsDataURL(file);
        }
    });

    applyCropBtn.addEventListener('click', () => {
        if (cropper) {
            const canvas = cropper.getCroppedCanvas({
                width: 120, // Define o tamanho final da imagem
                height: 120,
            });
            photoPreview.src = canvas.toDataURL('image/png');
            cropModal.style.display = 'none';
        }
    });

    cancelCropBtn.addEventListener('click', () => {
        cropModal.style.display = 'none';
        if (cropper) {
            cropper.destroy();
        }
    });

    // Fechar o modal clicando fora dele
    window.onclick = function(event) {
        if (event.target === cropModal) {
            cropModal.style.display = "none";
            if (cropper) {
                cropper.destroy();
            }
        }
    }
});