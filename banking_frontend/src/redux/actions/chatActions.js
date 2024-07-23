import { createAsyncThunk } from '@reduxjs/toolkit';
import axios from 'axios';
import {
  sendMessageRequest,
  sendMessageSuccess,
  sendMessageFailure,
} from '../reducers/chatReducer';

export const sendMessage = createAsyncThunk(
  'chat/sendMessage',
  async (message, { dispatch }) => {
    dispatch(sendMessageRequest());
    try {
      const response = await axios.post('http://localhost:8000/api/chat/', { message });
      dispatch(sendMessageSuccess({ message, response: response.data.response }));
    } catch (error) {
      dispatch(sendMessageFailure(error.message));
    }
  }
);
