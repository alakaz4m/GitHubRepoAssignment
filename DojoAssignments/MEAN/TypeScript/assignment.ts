// var myNum: number = 5
// var myString: string = "Hello Universe"
// var myArr: number[1,2,3,4,5]
// var myObj = {name: "Bill"}
// var anythingVariable: any = "Hey"
// var anythingVariable: any = 25
// var arrayOne: number[true, false, true, true]
// var arrayTwo: number[1, 'abc', true, 2]
// var myNthObj = {x: 5, y: 10}

class MyNode{
  constructor(val: number){
    this.val = val
    this.random = Math.floor(Math.random() * 100000);
  }
  privateValueEncrypted(): number{
    this._priv = this.val;
    return this._priv * this.random;
  }
  sendError(): string{
    if(this.val != this._priv){
      return false;
    }
    else{
      return true;
    }
  }

}
var myNewNode = new MyNode(10);
console.log(myNewNode.val);
console.log(myNewNode.privateValueEncrypted());
console.log(myNewNode.sendError());
