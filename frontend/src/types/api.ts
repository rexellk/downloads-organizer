export interface FileInfo {
    name: string;
    size_mb: number;
    extension: string;
    age_days: number;
    created: string;
}

export interface FetchDownloadsResponse {
    files: FileInfo[];
    total_count: number;
    message: string;
}