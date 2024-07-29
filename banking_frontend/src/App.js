import React from 'react';
import { Route, Routes } from 'react-router-dom';
import Sidebar from './components/sidebar';
import ChatInterface from './components/ChatInterface';
import Dashboard from './components/Dashboard';
import UserManagement from './components/UserManagement';
import Transactions from './components/Transections';
import EmployeeActivity from './components/EmployeeActivity';
import CustomerInformation from './components/CustomerInformation';
import CreditCardTransactions from './components/CreditCardTransaction';
import LoanInformation from './components/LoanInformation';
import AccountInformation from './components/AccountInformation';
import './App.css';

const App = () => {
  return (
    <div className="app">
      <Sidebar />
      <div className="main-content">
        <Routes>
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/user-management" element={<UserManagement />} />
          <Route path="/transactions" element={<Transactions />} />
          <Route path="/employee-activity" element={<EmployeeActivity />} />
          <Route path="/customer-information" element={<CustomerInformation />} />
          <Route path="/credit-card-transactions" element={<CreditCardTransactions />} />
          <Route path="/loan-information" element={<LoanInformation />} />
          <Route path="/account-information" element={<AccountInformation />} />
          <Route path="/chat" element={<ChatInterface />} />
        </Routes>
      </div>
    </div>
  );
};

export default App;
