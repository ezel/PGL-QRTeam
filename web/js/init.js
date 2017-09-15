var rl, td;

function initPrimary() {
  var tbl1 = document.getElementById('tbl1');
  var tr_contents, tr_class = ['rankTD', 'nameTD', 'linkTD'];
  var tr_node;
  for (var i=0;i<rl.length;i++) {
    var teamCd = rl[i].battleTeam.battleTeamCd;
    // init tr_node
    tr_contents = [rl[i].ranking, rl[i].battleTeam.battleTeamName, createA(teamCd,'https://3ds.pokemon-gl.com/rentalteam/'+teamCd)];
    tr_node = createTr(tr_contents, tr_class);
    //tr_node.setAttribute('teamCd', teamCd);
    tr_node.id = teamCd;

    // event listen
    tr_node.addEventListener('click', function(){
      //console.log('clicked is:'+ this.className);
      updateSecondary(this.id);
      // clear all styles
      for (var j=0;j<tbl1.children.length;j++)
        tbl1.children[j].style.backgroundColor = '';

      // choosed style
      this.style.backgroundColor = 'red';
    });
    // init table1 with tr
    tbl1.appendChild(tr_node);
  }
}

function updateSecondary(teamCd) {
  var tbl2 = document.getElementById('tbl2');
  // clear tbl2
  // other way: can use replaceChild to keep <thead>
  tbl2.innerHTML = "";

  var detail = td[teamCd];
  var tr_node, tr_contents, tr_class = ['idTD','pmTD','genderTD','abTD','itemTD','wzTD','wzTD','wzTD','wzTD'];
  for (var i=0;i<detail.pokemonList.length;i++) {
    var pm = detail.pokemonList[i];
    tr_contents = [createPokemonIcon(pm.monsno, pm.formNo),pm.name, pm.gender, pm.tokusei, pm.itemName,
                   pm.waza1.name, pm.waza2.name, pm.waza3.name, pm.waza4.name];
    tr_node = createTr(tr_contents, tr_class);
    tbl2.appendChild(tr_node);
  }
}

initPrimary();
