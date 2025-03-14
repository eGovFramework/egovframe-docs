let co
let codeListings = document.querySelectorAll('.highlight');

for (let index = 0; index < codeListings.length; index++) {
  const codeSample = codeListings[index].querySelector('code');
  const copyButton = document.createElement('button');
  const buttonAttributes = {
    type: 'button',
    title: 'Copy to clipboard',
    'data-bs-toggle': 'tooltip',
    'data-bs-placement': 'top',
    'data-bs-container': 'body',
  };

  Object.keys(buttonAttributes).forEach((key) => {
    copyButton.setAttribute(key, buttonAttributes[key]);
  });

  copyButton.classList.add(
    'copy-to-clipboard-button'
  );

  copyButton.textContent='복사';

  copyButton.onclick = () => {
    copyCode(codeSample);
    copyButton.setAttribute('data-bs-original-title', '복사됨!');
    copyButton.textContent=copyButton.dataset.bsOriginalTitle;
  };

  copyButton.onmouseout = () => {
    copyButton.setAttribute('data-bs-original-title', '복사');
    copyButton.textContent=copyButton.dataset.bsOriginalTitle;
  };

  const buttonDiv = document.createElement('div');
  buttonDiv.classList.add('toolbar');
  buttonDiv.append(copyButton);
  codeListings[index].appendChild(buttonDiv);

  codeListings[index].classList.add('code-box');
}

const copyCode = (codeSample) => {
  navigator.clipboard.writeText(codeSample.textContent.trim() + '\n');
};
