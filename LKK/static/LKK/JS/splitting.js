  //Splitting html text
  let section = document.querySelector(".circle");
  let word = section.innerHTML;
  section.innerHTML = "";
  for (let index = 0; index < word.length; ++index) {
    let span = document.createElement("span");
    span.innerHTML = word[index];
    section.appendChild(span);
    span.style.cssText = "--size:" + word.length + ";--i:" + index;
  }