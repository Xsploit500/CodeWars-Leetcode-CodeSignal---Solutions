class RandomizedSet {
    values: number[];
    index: Map<number, number>;

    constructor() {
        this.values = [];
        this.index = new Map();
    }

    insert(val: number): boolean {
        if (this.index.has(val)) return false;
        this.index.set(val, this.values.length);
        this.values.push(val);
        return true;
    }

    remove(val: number): boolean {
        if (!this.index.has(val)) return false;
        const position = this.index.get(val);
        const last = this.values[this.values.length - 1];
        this.values[position] = last;
        this.index.set(last, position);
        this.values.pop();
        this.index.delete(val);
        return true;
    }

    getRandom(): number {
        const i = Math.floor(Math.random() * this.values.length);
        return this.values[i];
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * var obj = new RandomizedSet()
 * var param_1 = obj.insert(val)
 * var param_2 = obj.remove(val)
 * var param_3 = obj.getRandom()
 */