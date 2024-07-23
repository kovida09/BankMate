const initialState = {
    messages: [],
    loading: false,
    error: null,
  };
  
  const chatReducer = (state = initialState, action) => {
    switch (action.type) {
      case 'SEND_MESSAGE_REQUEST':
        return { ...state, loading: true, error: null };
      case 'SEND_MESSAGE_SUCCESS':
        return {
          ...state,
          loading: false,
          messages: [...state.messages, { text: action.payload, sender: 'bot' }],
        };
      case 'SEND_MESSAGE_FAILURE':
        return { ...state, loading: false, error: action.payload };
      default:
        return state;
    }
  };
  
  export default chatReducer;
  