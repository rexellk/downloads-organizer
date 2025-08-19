import React from 'react';
import { createRoot } from 'react-dom/client';
import DownloadsList from './components/downloads-list';

const App: React.FC = () => {
  return (
    <div>
      <h1>Downloads Organizer</h1>
      <DownloadsList />
    </div>
  );
};

const container = document.getElementById('root');
if (container) {
  const root = createRoot(container);
  root.render(<App />);
}