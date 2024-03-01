const FetchTypeEnum = {
    Json: "application/json",
    FormData: "multipart/form-data",
    Blob: "application/octet-stream"
}

// TODO interceptor
const interceptorRequest = ()=>{
    let headers = {}
    return headers
}
const interceptorResponse = ()=>{
    let response = {}
    return response
}

const fetchWrapper = async(url, params={}, options={})=>{
    const { method, input_type=FetchTypeEnum.Json, output_type } = options

    let headers = {
        // "Authorization": "Bearer " + localStorage.getItem('token')  // add token
    }
    let body = null
    const methods = method || "POST"

    switch(input_type) {
        case FetchTypeEnum.FormData:
            // headers["Content-Type"] = "multipart/form-data" // just omit it, browser will set it automatically
            body = new FormData()
            for(let key in params) { body.append(key, params[key]) }
            break
        case FetchTypeEnum.Blob:
            headers["Content-Type"] = "application/octet-stream"
            body = params   // body = fs.createReadStream(params)
            break
        case FetchTypeEnum.Json:
        default:
            headers["Content-Type"] = "application/json"
            body = JSON.stringify(params)
            break
    }

    // send request
    const op = { method: methods, headers: headers, body: body }
    // statistcs time use
    let request_start = new Date().getTime()
    const result = await fetch(url, op);
    let request_end = new Date().getTime()
    console.log(`[DEBUG] TimeUse : ${request_end-request_start}ms`);

    // debug info
    console.log(`[DEBUG] Send: <${url}>: ${op.headers["Content-Type"]}`);
    console.log(`[DEBUG] Resp: <${url}>: ${result.status} ${result.headers.get("content-type")}`)

    if(result.status != 200) {
        console.log(`[ERROR] ${result.status}`);
        return null;
    }

    const result_type = result.headers?.get("content-type")
    if (result_type && result_type.includes("application/json")) {
        return result.json();
    }
    if (result_type && result_type.includes("text/plain")) {
        return result.text();
    }
    if (result_type && result_type.includes("application/octet-stream")) {
        return result.blob();
    }
    // image/png .etc
    if (result_type && result_type.includes("image/")) {
        let arrayBuffer = await result.arrayBuffer()
        const buffer = Buffer.from(arrayBuffer);
        return buffer;
    }
    return result;
    
}
/*
    test code with python-fastapi:
    1/ test normal json request and normal json response
        class TestModel(BaseModel):
            info: str

        @app.post("/test_body")
        async def test_body(info: TestModel):
            return {"body": info}

        let r = await fetchWrapper("http://127.0.0.1:8000/test_body", {info:"111"})

    2/ test normal json request and download response
        // window.location.href = 'http://127.0.0.1:8000/download';
        class TestModel(BaseModel):
            path: str

        @app.post("/test_download")
        async def test_download(p: TestModel):
            return FileResponse(p.path)

        let r= await fetchWrapper("http://127.0.0.1:8000/test_download", {path:"./test.png"})
        let arrayBuffer = await r.arrayBuffer()
        const buffer = Buffer.from(arrayBuffer);
        fs.writeFileSync('output.png', buffer);

    3/ test form data request and normal json response
        @app.post("/test_form_data")
        async def test_form_data(info: str=Form()):
            return {"result": info}

        let r = await fetchWrapper("http://127.0.0.1:8000/test_form_data", 
            {info:"111"}, 
            {input_type: FetchTypeEnum.FormData})

    4/ test form data(upload file) request and normal json response
        @app.post("/test_upload")
        async def test_upload(fe: UploadFile):
            with open(fe.filename, "wb") as buffer:
                shutil.copyfileobj(fe.file, buffer)
            return {"filename": fe.filename}

        @app.post("/test_upload")
        async def test_upload(request: Request):
            data = await request.body()
            with open('received_file', 'wb') as f:
                f.write(data)
            return {"filename": 1}
        
        let fe = new File(["123"], "test.txt", {type: "text/plain"});
        const formData = new FormData(); formData.append("fe", fe);
        let r= await fetchWrapperOld("http://127.0.0.1:8000/test_upload", formData)

        (async ()=>{
        })()
    */