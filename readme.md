JSON형식

RequestJson
{
    Type : (GET or CHECK),
    // Check일때 Product넣으셈
    Product : ProductCode (String),
    Key : Key(String)
    //GET Type일때 추가
    Code : Code(String)
}

ResultJson
{
    Type : (GET or CHECK),
    Product : ProductCode (String),
    //Chekc Type일때 추가
    Many : 수량(int),
    //Get Type일때 추가
    Result : (True or False) //True : 코드 맞음, False : 코드 틀림
}