import React from 'react';
import { Link } from 'react-router-dom';
import './Sidebar.css';

const Sidebar = () => {
  return (
    <div className="sidebar">
      <h2>BankMate</h2>
      <ul>
        <li><Link to="/user-transactions">User Transactions</Link></li>
        <li><Link to="/user-profile">User Profile</Link></li>
        <li><Link to="/activity">Your Activity</Link></li>
        <li><Link to="/settings">Settings</Link></li>
      </ul>
      <div className="sidebar-bottom">
        <button>Manage Your Widgets</button>
        <button>Log Out</button>
      </div>
    </div>
  );
};

export default Sidebar;
