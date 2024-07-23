import React from 'react';
import { Link } from 'react-router-dom';

const Dashboard = () => {
  return (
    <div className="dashboard">
      <h1>Dashboard</h1>
      {/* Add dashboard content here */}
      <div className="options">
        <Link to="/customer-information">Customer Information</Link>
        <Link to="/credit-card-transactions">Credit Card Transactions</Link>
        <Link to="/loan-information">Loan Information</Link>
        <Link to="/account-information">Account Information</Link>
      </div>
    </div>
  );
};

export default Dashboard;
