import request from "request";

async function req(url, method, requestData) {
    request({
            url: url,
            method: method,
            json: true,
            headers: {
                "content-type": "application/json",
            },
            body: JSON.stringify(requestData)
        },
        function (error, response, body) {
            if (!error && response.statusCode == 200) {
                console.log("responseData: ", body); // 请求成功的处理逻辑
            }
        });
}

export default req;