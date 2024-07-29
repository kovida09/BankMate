import { configureStore } from '@reduxjs/toolkit';
import chatReducer from './reducers/chatReducers';

const store = configureStore({
  reducer: {
    chat: chatReducer,
  },
});

export default store;
