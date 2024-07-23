import { combineReducers } from 'redux';
import chatReducer from './chatReducer';

const rootReducer = combineReducers({
  chat: chatReducer,
  // Add other reducers here
});

export default rootReducer;
