// let input = require("fs").readFileSync("/dev/stdin").toString()trim();
let input = require("fs").readFileSync("data.txt").toString().trim();

input = Number(input);
class Node {
  constructor(data, next = null, prev = null) {
    this.data = data;
    this.next = next;
    this.prev = prev;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.size = 0;
  }

  push(data) {
    let node = new Node(data);

    if (!this.head) {
      this.head = node;
    } else {
      this.tail.next = node;
      node.prev = this.tail;
    }
    this.tail = node;
    this.size++;
  }

  getHead() {
    return this.head.data;
  }

  removeHead() {
    this.head = this.head.next;
    this.head.prev = null;
    this.size--;
  }
  getSize() {
    return this.size;
  }
}

const list = new LinkedList();

for (let i = 1; i <= input; i++) {
  list.push(i);
}

while (list.getSize() !== 1) {
  list.removeHead();
  list.push(list.getHead());
  list.removeHead();
}

console.log(list.getHead());
