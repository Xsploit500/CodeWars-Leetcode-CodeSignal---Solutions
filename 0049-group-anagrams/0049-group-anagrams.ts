function groupAnagrams(strs: string[]): string[][] {
    const groups = new Map();
    for (const string of strs){
        const key = string.split('').sort().join('');
        if (!groups.has(key)) groups.set(key, [])
        groups.get(key).push(string);
    }
    return Array.from(groups.values());
};