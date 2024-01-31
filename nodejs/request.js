import qs from 'qs'
import fs from 'fs'

// front may give

// front may get

// intern needL localstorage:token
// headers["Content-Type"] = "application/octet-stream"?
const fetchWrapper = async (url, params, option={}) => {
    let method = option.method || "POST"
    let is_blob = option.is_blob || false
    let headers = { 
        "Content-Type": "application/json",     // default to json
        // "Authorization": "Bearer " + localStorage.getItem('token')  // add token
    }
    let body = params

    // let browser set Content-Type automatically when params is FormData
    // multipart/form-data?
    if(body instanceof FormData) {
        delete headers['Content-Type'];
    } 
    if(is_blob) {
        headers["Content-Type"] = "application/octet-stream"
    } else {    // is json
        body = JSON.stringify(params)
    }

    // send request
    const op = { method: method, headers: headers, body: body }
    const result = await fetch(url, op);

    // debug info
    console.log(`[DEBUG] Send: ${url}: ${op}`);
    console.log(`[DEBUG] Resp: ${url}: ${result.headers.get("content-type")}`)
    
    const result_type = result.headers.get("content-type")
    if (result_type && result_type.includes("application/json")) {
        return result.json();
    }
    // if (result_type && result_type.includes("text/plain")) {
    //     return result.text();
    // }
    // if (result_type && result_type.includes("application/octet-stream")) {
    //     return result.blob();
    // }
    return result;
}

/*
    test code with python-fastapi:
    1/ test normal json request and normal json response
        class TestModel(BaseModel):
            name: str
            age: int

        @app.post("/test_body")
        async def test_body(info: TestModel):
            return {"body": info}

        let r = await fetchWrapper("http://127.0.0.1:8000/test_body", {name:"111", age:10})

    2/ test normal json request and download response
        // window.location.href = 'http://127.0.0.1:8000/download';
        class TestModel(BaseModel):
            path: str

        @app.post("/test_download")
        async def test_download(p: TestModel):
            return FileResponse(p.path)

        let r= await fetchWrapper("http://127.0.0.1:8000/test_download", {path:"./test.txt"})

    3/ test form data request and normal json response
        @app.post("/test_form_data")
        async def test_form_data(a: str=Form()):
            return {"result": a}

        let formData = new FormData(); p.append("a", "b");
        let r = await fetchWrapper("http://127.0.0.1:8000/test_form_data", formData)

    4/ test form data(upload file) request and normal json response
        @app.post("/test_upload")
        async def test_upload(fe: UploadFile):
            with open(fe.filename, "wb") as buffer:
                shutil.copyfileobj(fe.file, buffer)
            return {"filename": fe.filename}
        
        let fe = new File(["123"], "test.txt", {type: "text/plain"});
        const formData = new FormData(); formData.append("fe", fe);
        let r= await fetchWrapper("http://127.0.0.1:8000/test_upload", formData)
    */
(async ()=>{
    // let r= await fetchWrapper("http://127.0.0.1:8000/test_download", {path:"./test.b"})
    // create a Blob with content="asd"
    
    // let blob = new Blob(["asd"], {type: "text/plain"});
    // let fe = new File([blob], "test.b2", {type: "text/plain"});

    // const fe = fs.readFileSync("./1.png", 'utf8')
    // let r= await fetchWrapper("http://127.0.0.1:8000/test_upload", fe, {is_blob: true})

    // let r= await fetchWrapper("http://127.0.0.1:8000/test_download", {path:"./b"})
    // let t = await r.text()
    // console.log(r)
})()