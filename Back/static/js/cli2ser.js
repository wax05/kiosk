function client2server(url,data){
    axios.post(url,data)
    .then((response)=>{
        return response
    });
    .catch((error)=>{
        return error
    });
}