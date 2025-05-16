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

  /* 복사완료 표시를 mouseover 시 변경이 아닌 복사 후 1초 후에 아이콘 변경*/
  copyButton.onclick = () => {
    copyCode(codeSample);
    copyButton.classList.add("after");
    setTimeout(function(){
      copyButton.classList.remove("after");
    },1000);

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
