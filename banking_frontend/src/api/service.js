import axios from 'axios';

const API_URL = 'http://localhost:8000/api';

export const getAccountInformation = () => axios.get(`${API_URL}/account-information/`);
export const getTransactionInformation = () => axios.get(`${API_URL}/transaction-information/`);
export const getLoanInformation = () => axios.get(`${API_URL}/loan-information/`);
export const getCreditCardInformation = () => axios.get(`${API_URL}/credit-card-information/`);
export const getcustomerInformation = () => axios.get(`${API_URL}/customer-information/`);