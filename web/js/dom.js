function createTd(text, className=false) {
  var td = document.createElement('td');
  if ((typeof(text) !== "object") || (text === null))
    td.textContent = text;
  else
    td.appendChild(text);
  if (className) td.className = className;
  return td;
}

function createTh(text, className=false) {
  var th = document.createElement('th');
  th.textContent = text;
  if (className) th.className = className;
  return th;
}

function createTr(textArray, classArray) {
  var tr = document.createElement('tr');
  for (var i=0;i<textArray.length;i++) {
    tr.appendChild(createTd(textArray[i], classArray[i]));
  }
  return tr;
}

function createTrWithTh(textArray, classArray=[]) {
  var tr = document.createElement('tr');
  tr.appendChild(createTh(textArray[0], classArray[0]));
  tr.appendChild(createTd(textArray[1], classArray[1]));
  return tr;
}

function createA(text, href, className=false) {
  var a = document.createElement('a');
  a.href = href;
  a.textContent = text;
  if (className) a.className = className;
  return a;
}

function createTdForRanking(rankingStr) {
  var div = document.createElement('div');
  // for each ranking
  var rankingHTML = rankingStr.replace(/,/g, '<br/>');
  div.innerHTML = rankingHTML;
  return div;
}

function createTdForTeamPreview(teamCd) {
  var div = document.createElement('div');
  for (var j=0;j<td[teamCd].pokemonList.length;j++) {
    div.appendChild(createPokemonIcon(td[teamCd].pokemonList[j].monsno, td[teamCd].pokemonList[j].formNo));
  }
  return div;
}

function createTdForTypePreview(teamCd) {
  var div = document.createElement('div');
  for (var j=0;j<td[teamCd].pokemonList.length;j++) {
    div.appendChild(createTypeIcon(td[teamCd].pokemonList[j].typeId1, td[teamCd].pokemonList[j].typeId2));
  }
  return div;
}

function createCheckbox(seasonLArray=[1,2,3]) {
  var schkb = document.getElementById("seasons");
  for (var i=0; i<seasonLArray.length; i++) {
    sbox = document.createElement('input');
    sbox.type = "checkbox";
    sbox.checked = true;
    sbox.id = "S" + seasonLArray[i];
    sbox.name = "interest";
    sbox.value = sbox.id;
    slabel = document.createElement('label');
    slabel.htmlFor = sbox.id;
    slabel.textContent = "Season " + seasonLArray[i];
    seasons.appendChild(sbox);
    seasons.appendChild(slabel);
    if (i%2) seasons.appendChild(document.createElement('br'));
  }
}

function transferGender(gender) {
  switch(gender) {
  case 0:
    return 'M';
  case 1:
    return 'F';
  case 2:
  default:
    return '';
  }
}

function getPokemonIcon(pmID, formID=0) {
  var altnum = {
    25: 804 + 2,//pikachubelle
    25: 804 + 3,//pikachulibre
    25: 804 + 4,//pikachuphd
    25: 804 + 5,//pikachupopstar
    25: 804 + 6,//pikachurockstar
    25: 804 + 7,//pikachucosplay
    386: 804 + 38,//deoxysattack
    386: 804 + 39,//deoxysdefense
    386: 804 + 40,//deoxysspeed
    412: 804 + 41,//burmysandy
    412: 804 + 42,//burmytrash
    413: 804 + 43,//wormadamsandy
    413: 804 + 44,//wormadamtrash
    421: 804 + 45,//cherrimsunshine
    422: 804 + 46,//shelloseast
    423: 804 + 47,//gastrodoneast
    479: 804 + 48,//rotomfan
    479: 804 + 49,//rotomfrost
    479: 804 + 50,//rotomheat
    479: 804 + 51,//rotommow
    479: 804 + 52,//rotomwash
    487: 804 + 53,//giratinaorigin
    492: 804 + 54,//shayminsky
    521: 804 + 55,//unfezantf
    550: 804 + 56,//basculinbluestriped
    555: 804 + 57,//darmanitanzen
    592: 804 + 64,//frillishf
    593: 804 + 65,//jellicentf
    641: 804 + 66,//tornadustherian
    642: 804 + 67,//thundurustherian
    645: 804 + 68,//landorustherian
    646: 804 + 69,//kyuremblack
    646: 804 + 70,//kyuremwhite
    647: 804 + 71,//keldeoresolute
    648: 804 + 72,//meloettapirouette
    666: 804 + 73,//vivillonarchipelago
    666: 804 + 74,//vivilloncontinental
    666: 804 + 75,//vivillonelegant
    666: 804 + 76,//vivillonfancy
    666: 804 + 77,//vivillongarden
    666: 804 + 78,//vivillonhighplains
    666: 804 + 79,//vivillonicysnow
    666: 804 + 80,//vivillonjungle
    666: 804 + 81,//vivillonmarine
    666: 804 + 82,//vivillonmodern
    666: 804 + 83,//vivillonmonsoon
    666: 804 + 84,//vivillonocean
    666: 804 + 85,//vivillonpokeball
    666: 804 + 86,//vivillonpolar
    666: 804 + 87,//vivillonriver
    666: 804 + 88,//vivillonsandstorm
    666: 804 + 89,//vivillonsavanna
    666: 804 + 90,//vivillonsun
    666: 804 + 91,//vivillontundra
    678: 804 + 115,//meowsticf
    19: 804 + 119,//rattataalola
    20: 804 + 120,//raticatealola
    26: 804 + 121,//raichualola
    27: 804 + 122,//sandshrewalola
    28: 804 + 123,//sandslashalola
    37: 804 + 124,//vulpixalola
    38: 804 + 125,//ninetalesalola
    50: 804 + 126,//diglettalola
    51: 804 + 127,//dugtrioalola
    52: 804 + 128,//meowthalola
    53: 804 + 129,//persianalola
    74: 804 + 130,//geodudealola
    75: 804 + 131,//graveleralola
    76: 804 + 132,//golemalola
    88: 804 + 133,//grimeralola
    89: 804 + 134,//mukalola
    103: 804 + 135,//exeggutoralola
    105: 804 + 136,//marowakalola
    658: 804 + 137,//greninjaash
    718: 804 + 138,//zygarde10
    718: 804 + 139,//zygardecomplete
    741: 804 + 140,//oricoriopompom
    741: 804 + 141,//oricoriopau
    741: 804 + 142,//oricoriosensu
    745: 804 + 143,//lycanrocmidnight
    746: 804 + 144,//wishiwashischool
    774: 804 + 145,//miniormeteor
    774: 804 + 146,//miniororange
    774: 804 + 147,//minioryellow
    774: 804 + 148,//miniorgreen
    774: 804 + 149,//miniorblue
    774: 804 + 150,//miniorviolet
    774: 804 + 151//miniorindigo
  };
  if (pmID<0) pmID=0;
  num = pmID;
  if (formID > 0) {
    num = altnum[pmID];
  }
  var top = Math.floor(num / 12) * 30;
  var left = (num % 12) * 40;
  return 'background:transparent url(images/pm-sheet.png) no-repeat scroll -' + left + 'px -' + top + 'px';
}

function createPokemonIcon(pmID, formID) {
  var span = document.createElement('span');
  span.style = getPokemonIcon(pmID, formID);
  span.className = 'pokemonIcon';
  return span;
}

function getTypeIcon(typeId) {
  var typeCharts = {
    0 : 'typeNone',
    1 : 'typeNormal',
    2 : 'typeFighting',
    3 : 'typeFire',
    4 : 'typeIce',
    5 : 'typeElectric',
    6 : 'typeFlying',
    7 : 'typeGrass',
    8 : 'typeGround',
    9 : 'typePoison',
    10 : 'typeBug',
    11 : 'typeDark',
    12 : 'typeWater',
    13 : 'typePsychic',
    14 : 'typeDragon',
    15 : 'typeRock',
    16 : 'typeGhost',
    17 : 'typeSteel',
    18 : 'typeFairy'
  };
  return typeCharts[typeId];
}

function createTypeIcon(typeId1, typeId2) {
  var spanA = document.createElement('span');
  spanA.className = 'typeIcon';
  var spanL = document.createElement('span');
  var spanR = document.createElement('span');
  spanL.className = 'typeIconInner typeLeft '+ getTypeIcon(typeId1);
  spanR.className = 'typeIconInner typeRight ';
  if (typeId2 > 0) {
    spanR.className += getTypeIcon(typeId2);
  } else {
    spanR.className += getTypeIcon(typeId1);
  }
  spanA.appendChild(spanL);
  spanA.appendChild(spanR);
  return spanA;
}
