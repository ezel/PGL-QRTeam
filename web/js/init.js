var rl, td;

function initPrimary() {
  var tbl1 = document.getElementById('tbl1');
  var tr_contents, tr_class = ['rankTD', 'prevTD'];
  var tr_node;
  for (var i=0;i<rl.length;i++) {
    var teamCd = rl[i].battleTeam.battleTeamCd;
    // init tr_node
    let team_prev = createTdForTeamPreview(teamCd);
    tr_contents = [createTdForRanking(rl[i].ranking), team_prev];
    tr_node = createTr(tr_contents, tr_class);
    //tr_node.setAttribute('teamCd', teamCd);
    tr_node.id = i;

    // event listen
    tr_node.addEventListener('click', function(){
      //console.log('clicked is:'+ this.className);
      updateSecondary(this.id);
      updateThird(this.id);
      // clear all styles
      for (var j=0;j<tbl1.children.length;j++)
        tbl1.children[j].style.backgroundColor = '';

      // choosed style
      this.style.backgroundColor = '#e64946';
    });
    // init table1 with tr
    tbl1.appendChild(tr_node);
  }
}

function updateSecondary(rlId) {
  var tbl2 = document.getElementById('tbl2');
  var teamCd = rl[rlId].battleTeam.battleTeamCd;
  // clear tbl2
  // other way: can use replaceChild to keep <thead>
  tbl2.innerHTML = "";

  var detail = td[teamCd];
  var tr_node, tr_contents, tr_class = ['idTD','pmTD','genderTD','abTD','itemTD','wzTD','wzTD','wzTD','wzTD'];
  for (var i=0;i<detail.pokemonList.length;i++) {
    var pm = detail.pokemonList[i];
    tr_contents = [createPokemonIcon(pm.monsno, pm.formNo),pm.name, transferGender(pm.gender), pm.tokusei, pm.itemName,
                   pm.waza1.name, pm.waza2.name, pm.waza3.name, pm.waza4.name];
    tr_node = createTr(tr_contents, tr_class);
    tbl2.appendChild(tr_node);
  }
}

function updateThird(rlId) {
  var tbl3 = document.getElementById('tbl3');
  tbl3.innerHTML = "";
  var teamCd = rl[rlId].battleTeam.battleTeamCd;
  var detail = td[teamCd];
  tbl3.appendChild(createTrWithTh(['Rank', rl[rlId].ranking.replace(/,/g, '  ')]));
  tbl3.appendChild(createTrWithTh(['Name', detail.battleTeam.battleTeamName]));
  tbl3.appendChild(createTrWithTh(['Message', detail.battleTeam.message]));
  tbl3.appendChild(createTrWithTh(['Usage', detail.battleTeam.winCount +' / ' + detail.battleTeam.useCount]));
  tbl3.appendChild(createTrWithTh(['Trainer', detail.trainer.trainerName + ' (' + detail.trainer.trainerNameRuby + ')']));
  tbl3.appendChild(createTrWithTh(['Country', detail.trainer.countryCode]));
  tbl3.appendChild(createTrWithTh(['Link', createA(teamCd, 'https://3ds.pokemon-gl.com/rentalteam/'+teamCd)]));
}

function filterTeamWithInput() {
  var input, filter, table, tr;
  input = document.getElementById("fInput");
  filter = input.value.toUpperCase();
  table = document.getElementById("tbl1");
  tr = table.getElementsByTagName("tr");

  // Loop through all table rows, and hide those who don't match the search query
  for (let i = 0; i < tr.length; i++) {
    var teamCd = rl[i].battleTeam.battleTeamCd;
    if (rl[i]) {
      if ((matchCheckbox(rl[i].ranking)) &&
          ((rl[i].trainer.trainerName.toUpperCase().indexOf(filter) > -1 ) ||
           (rl[i].trainer.trainerNameRuby.toUpperCase().indexOf(filter) > -1 ) ||
           (rl[i].trainer.countryCode.indexOf(filter) > -1 ) ||
           (td[teamCd].pokemonList.map(function(l) { return l.name.toUpperCase();}).join().indexOf(filter) > -1) ||
           (td[teamCd].pokemonList.map(function(l) { return l.name.replace(/ /g,"").toUpperCase();}).join().indexOf(filter) > -1)
          )
         ) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}

function initCheckbox() {
  var result = [];
  // search rankinglist
  for (let i=0;i<rl.length;i++) {
    let r = rl[i].ranking;
    let sidx = r.indexOf("S");
    while (sidx>0) {
      let sid = parseInt(r.substr(sidx+1, r.indexOf(".",sidx)-sidx));
      if (result.indexOf(sid)<0) result.push(sid);
      sidx = r.indexOf("S", sidx+1);
    }
  }
  result.sort();
  createCheckbox(result);

  // add event listener
  var fcheckbox = document.getElementById('fCheckbox');
  var inputs = fcheckbox.getElementsByTagName('input');
  for (let i=0;i<inputs.length;i++) {
    inputs[i].addEventListener('change', function(e) {
      filterTeamWithInput();
    });
  }
}

function matchCheckbox(ranking) {
  var filters = getCheckboxValue();
  // no interests
  if (filters.length==0) {
    return false;
  }
  // compare 2 array
  for(let j=0;j<filters.length;j++) {
    if (ranking.indexOf(filters[j]) > -1 ) {
      return true;
    }
  }
  return false;
}

function getCheckboxValue() {
  var result = [];
  var fcheckbox = document.getElementById('fCheckbox');
  var inputs = fcheckbox.getElementsByTagName('input');
  for (let i=0;i<inputs.length;i++) {
    if (inputs[i].checked) {
      result.push(inputs[i].value);
    }
  }
  return result;
}

initCheckbox();
initPrimary();
