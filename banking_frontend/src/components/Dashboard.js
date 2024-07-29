import React from 'react';
import { Link } from 'react-router-dom';
import './Dashboard.css';

const Dashboard = () => {
  return (
    <div className="dashboard">
      <h1>Your Banking Guide</h1>
      <div className="options">
        <Link to="/loan-information" className="option">Loan Details</Link>
        <Link to="/account-information" className="option">Active Accounts</Link>
        <Link to="/credit-card-transactions" className="option">Credit Card Details</Link>
        <Link to="/dashboard" className="option">Dashboard</Link>
      </div>
    </div>
  );
};

export default Dashboard;
