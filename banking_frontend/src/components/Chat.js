import React, { useState } from 'react';
import axios from 'axios';

const Chat = () => {
    const [query, setQuery] = useState('');
    const [response, setResponse] = useState('');

    const handleQueryChange = (e) => {
        setQuery(e.target.value);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const res = await axios.post('http://localhost:8000/api/chat/', { query });
            setResponse(res.data.response);
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <input type="text" value={query} onChange={handleQueryChange} />
                <button type="submit">Send</button>
            </form>
            <div>
                {response}
            </div>
        </div>
    );
};

export default Chat;
