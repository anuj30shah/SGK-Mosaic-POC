// After images are generated, populate the text inputs with the default values
function populateTextInputs(tagline, adv1, adv2, adv3) {
    document.getElementById('text1').value = tagline;
    document.getElementById('text2').value = adv1;
    document.getElementById('text3').value = adv2;
    document.getElementById('text4').value = adv3;
}

document.getElementById("image-form").addEventListener("submit", function(event) {
    event.preventDefault();
    
    const formData = new FormData(event.target);
    
    fetch("/", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        populateTextInputs(data.tagline, data.adv1, data.adv2, data.adv3);
        const imageDisplay = document.getElementById("image-display");

        imageDisplay.classList.remove("flex-layout");
        imageDisplay.classList.add("grid-layout");

        imageDisplay.innerHTML = '';
        
        data.images.forEach((imagePath, index) => {
            const img = document.createElement("img");
            img.src = imagePath;
            img.alt = `Generated Image ${index + 1}`;
            img.classList.add("grid-image"); // Apply grid-specific class
            img.onclick = () => outpaintImage(imagePath);
            imageDisplay.appendChild(img);
        });
    });
});

function outpaintImage(imagePath) {
    const formData = new FormData();

    const outpaintScale = document.getElementById("outpaint-scale").value;
    const orientation = document.getElementById("orientation").value;

    formData.append("image_path", imagePath);
    formData.append("product", document.getElementById("product").value);
    formData.append("bg_color", document.getElementById("bg_color").value);

    formData.append("outpaint-scale", outpaintScale);
    formData.append("orientation", orientation);

    const imageDisplay = document.getElementById("image-display");

    imageDisplay.classList.remove("grid-layout");
    imageDisplay.classList.add("flex-layout");

    imageDisplay.innerHTML = ''; // Clear previous content

    fetch("/outpaint", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        const img = document.createElement("img");
        img.src = data.outpainted_image;
        img.alt = "Outpainted Image";
        img.classList.add("outpainted-image");
        imageDisplay.appendChild(img);
    })
    .catch(error => {
        console.error('Error:', error);
    });
    
}

document.getElementById('add-text-btn').addEventListener('click', function() {
    const texts = [
        document.getElementById('text1').value,
        document.getElementById('text2').value,
        document.getElementById('text3').value,
        document.getElementById('text4').value
    ];

    const fontSizes = [
        document.getElementById('font-size1').value + 'px',
        document.getElementById('font-size2').value + 'px',
        document.getElementById('font-size3').value + 'px',
        document.getElementById('font-size4').value + 'px'
    ];

    document.querySelectorAll('.draggable-text').forEach(el => el.remove());

    for (let index = 0; index < texts.length; index++) {
        const textElem = document.createElement('div');
        textElem.classList.add('draggable-text');
        textElem.textContent = texts[index];
        textElem.style.position = 'absolute';
        textElem.style.left = `${index * 100 + 750}px`;
        textElem.style.top = `${index * 50 + 750}px`;
        textElem.style.fontSize = fontSizes[index];
        textElem.id = `text-elem-${index}`;
        textElem.setAttribute('data-index', index);  // Set data-index attribute

        textElem.addEventListener('mousedown', dragMouseDown);

        document.getElementById('image-display').appendChild(textElem);
    }
});

// Live update of font size
document.getElementById('font-size1').addEventListener('input', function() {
    const elem = document.getElementById('text-elem-0');
    if (elem) elem.style.fontSize = this.value + 'px';
});

document.getElementById('font-size2').addEventListener('input', function() {
    const elem = document.getElementById('text-elem-1');
    if (elem) elem.style.fontSize = this.value + 'px';
});

document.getElementById('font-size3').addEventListener('input', function() {
    const elem = document.getElementById('text-elem-2');
    if (elem) elem.style.fontSize = this.value + 'px';
});

document.getElementById('font-size4').addEventListener('input', function() {
    const elem = document.getElementById('text-elem-3');
    if (elem) elem.style.fontSize = this.value + 'px';
});





function dragMouseDown(e) {
    e.preventDefault();
    const textElem = e.target;

    // Get the initial mouse position and element's position
    let pos3 = e.clientX;
    let pos4 = e.clientY;
    let rect = textElem.getBoundingClientRect();

    // Attach listeners for mouse movement and release
    document.onmousemove = (event) => elementDrag(event, textElem, rect, pos3, pos4);
    document.onmouseup = closeDragElement;
}

function elementDrag(e, textElem, rect, pos3, pos4) {
    e.preventDefault();

    // Calculate the new cursor position
    let pos1 = pos3 - e.clientX;
    let pos2 = pos4 - e.clientY;

    // Update the element's position based on the movement
    textElem.style.left = `${rect.left - pos1}px`;
    textElem.style.top = `${rect.top - pos2}px`;

    // Update the initial positions
    pos3 = e.clientX;
    pos4 = e.clientY;
}

function closeDragElement() {
    // Stop moving when the mouse button is released
    document.onmouseup = null;
    document.onmousemove = null;
}


// Live update text content
// Live update text content using data-index
const inputs = document.querySelectorAll('#text-form input[type="text"]');
inputs.forEach((input, index) => {
    input.setAttribute('data-index', index);  // Set data-index attribute
    input.addEventListener('input', function() {
        const dataIndex = this.getAttribute('data-index');
        const textElem = document.querySelector(`.draggable-text[data-index="${dataIndex}"]`);
        if (textElem) {
            textElem.textContent = this.value;
        }
    });
});