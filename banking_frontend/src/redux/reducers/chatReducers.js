const initialState = {
  messages: [],
  loading: false,
  error: null,
};

const chatReducer = (state = initialState, action) => {
  switch (action.type) {
    case 'SEND_MESSAGE':
      return {
        ...state,
        messages: [...state.messages, { text: action.payload, sender: 'user' }],
      };
    case 'BOT_RESPONSE':
      return {
        ...state,
        messages: [...state.messages, { text: action.payload, sender: 'bot' }],
      };
    case 'SET_LOADING':
      return {
        ...state,
        loading: action.payload,
      };
    case 'SET_ERROR':
      return {
        ...state,
        error: action.payload,
      };
    default:
      return state;
  }
};

export default chatReducer;
