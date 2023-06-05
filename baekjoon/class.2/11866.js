// let input = fs.readFileSync("/dev/stdin").toString();
let num = require("fs").readFileSync("data.txt").toString().trim().split(" ");

class Node {
  constructor(data, next = null) {
    this.data = data;
    this.next = next;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
    this.size = 0;
  }

  insertFirst(data) {
    this.head = new Node(data, this.head);
    this.size++;
  }

  insertLast(data) {
    this;
  }
}
