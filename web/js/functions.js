function createTd(text, className="") {
  var td = document.createElement('td');
  if (typeof(text) !== "object")
    td.textContent = text;
  else
    td.appendChild(text);
  if (className) td.className = className;
  return td;
}

function createTr(textArray, classArray) {
  var tr = document.createElement('tr');
  for (var i=0;i<textArray.length;i++) {
    tr.appendChild(createTd(textArray[i], classArray[i]));
  }
  return tr;
}

function createA(text, href, className=false) {
  var a = document.createElement('a');
  a.href = href;
  a.textContent = text;
  if (className) a.className = className;
  return a;
}
