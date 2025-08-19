import { FetchDownloadsResponse } from "../../types/api";

const API_BASE = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'; // Fallback to localhost

export const fetchFiles = async (): Promise<FetchDownloadsResponse> => {
  const response = await fetch(`${API_BASE}/api/files`);
  return response.json();
};
