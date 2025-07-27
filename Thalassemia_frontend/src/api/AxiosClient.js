import axios from 'axios';

const AxiosClient = axios.create({
    baseURL: 'http://172.20.215.148:5000', // Base URL for your Flask server
    headers: {
        'Content-Type': 'application/json',
    },
});

export default AxiosClient;