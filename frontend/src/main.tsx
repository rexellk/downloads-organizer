import React from 'react';
import { createRoot } from 'react-dom/client';
import DisplayBox from './components/display-box';

const App: React.FC = () => {
  return (
    <div>
      <h1>Downloads Organizer</h1>
      <DisplayBox text="Welcome to the Downloads Organizer!" />
    </div>
  );
};

const container = document.getElementById('root');
if (container) {
  const root = createRoot(container);
  root.render(<App />);
}