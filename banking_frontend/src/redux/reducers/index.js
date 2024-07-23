import { combineReducers } from 'redux';
import chatReducer from './chatReducers';

const rootReducer = combineReducers({
  chat: chatReducer,
  // Add other reducers here
});

export default rootReducer;
