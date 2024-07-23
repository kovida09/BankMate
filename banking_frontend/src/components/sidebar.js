import React from 'react';
import { NavLink } from 'react-router-dom';
import './Sidebar.css';

const Sidebar = () => {
  return (
    <div className="sidebar">
      <nav>
        <ul>
          <li><NavLink to="/dashboard">Dashboard</NavLink></li>
          <li><NavLink to="/user-management">User Management</NavLink></li>
          <li><NavLink to="/transactions">Transactions</NavLink></li>
          <li><NavLink to="/employee-activity">Employee Activity</NavLink></li>
          <li><NavLink to="/customer-information">Customer Information</NavLink></li>
          <li><NavLink to="/credit-card-transactions">Credit Card Transactions</NavLink></li>
          <li><NavLink to="/loan-information">Loan Information</NavLink></li>
          <li><NavLink to="/account-information">Account Information</NavLink></li>
        </ul>
      </nav>
      <div className="sidebar-bottom">
        <NavLink to="/settings">Settings</NavLink>
        <NavLink to="/notifications">Notifications</NavLink>
      </div>
    </div>
  );
};

export default Sidebar;
