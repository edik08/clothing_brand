const serverUrl = `127.0.0.1:8000`;

async function getAllBrands() {
    let response = await fetch(
        `${serverUrl}\getAllProducts`,
        {
            method: "GET",

            headers: {
                "Content-Type":"application/json"
            }
        });
}