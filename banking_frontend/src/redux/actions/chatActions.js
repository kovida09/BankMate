import axios from 'axios';

export const sendMessage = (message) => async (dispatch) => {
  dispatch({ type: 'SEND_MESSAGE_REQUEST' });

  try {
    const response = await axios.post('http://localhost:8000/api/chat/', { query: message });
    dispatch({ type: 'SEND_MESSAGE_SUCCESS', payload: response.data.response });
  } catch (error) {
    dispatch({ type: 'SEND_MESSAGE_FAILURE', payload: error.message });
  }
};
