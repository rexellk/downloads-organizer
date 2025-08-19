import { FetchDownloadsResponse } from "../../types/api";

const API_BASE = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'; // Fallback to localhost

export const fetchFiles = async (): Promise<FetchDownloadsResponse> => {
  console.log('Fetching from:', `${API_BASE}/api/files`);
  const response = await fetch(`${API_BASE}/api/files`);
  console.log('Response status:', response.status);
  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }
  const data = await response.json();
  console.log('API response:', data);
  return data;
};
