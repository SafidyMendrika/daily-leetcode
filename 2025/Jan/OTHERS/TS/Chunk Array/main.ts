type JSONValue = null | boolean[] | number[] | string[] | JSONValue[] | { [key: string]: JSONValue };
type Obj = Record<string, JSONValue> | Array<JSONValue>;

function chunk(arr: Obj[], size: number): Obj[][] {
    const result : Obj[][] = [];
    let temp : Obj[] = [];

    for (let i = 0 ; i < arr.length ; i++){
        if (temp.length === size){
            result.push(temp);
            temp = [];
        }
        temp.push(arr[i]);
    }

    if (temp.length > 0){
        result.push(temp);
    }
    return result;
};

