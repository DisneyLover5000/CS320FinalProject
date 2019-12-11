
class ListItem{
  constructor(item){
    this.item = item;
  }

  show(){
    console.log(this.item,);

  }

}


var grabeditem;

class List{
  constrouctor(ListItem){
    this.listItem=[];


  }
  grabListItem(Item){
    'use strict';

    for (let j = 0; j < process.argv.length; j++) {
      console.log(j + ' -> ' + (process.argv[j]));
    }
    // grab item from input process.argv[j]

  }
  addListItem(Item){

//for (var i=0; i<= this.menuItem.length; i++){
    Item.grabListItem(Item)=grabeditem;
    this.listItem.push(grabeditem);
//}
  }



}

const Item = new List();
Item.addListItem(grabbeditem);
Item.addListItem(grabbeditem);
Item.addListItem(grabbeditem);
Item.addListItem(grabbeditem);
console.log(Item);



