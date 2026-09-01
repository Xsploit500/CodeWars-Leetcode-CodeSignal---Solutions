function topKFrequent(nums: number[], k: number): number[] {
    const count = new Map();
    for (const num of nums) count.set(num, (count.get(num) || 0) + 1);

    const buckets = Array.from({length: nums.length + 1}, () => []);
    for (const [val, freq] of count) buckets[freq].push(val);

    const result = [];
    for (let freq = buckets.length - 1; freq > 0 && result.length < k; freq--){
        for (const val of buckets[freq]){
            result.push(val)
            if (result.length === k) break;
        }
    }
    return result;
};