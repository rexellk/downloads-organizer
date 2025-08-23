# Frontend - Downloads Organizer UI

Modern React frontend for the Downloads Organizer application built with TypeScript, Vite, and a comprehensive UI component library.

## Technology Stack

- **React 19** - Frontend framework with latest features
- **TypeScript** - Type-safe JavaScript development
- **Vite** - Fast build tool and development server
- **Tailwind CSS v4** - Utility-first CSS framework
- **Radix UI** - Accessible component primitives
- **shadcn/ui** - Pre-built component library
- **Motion** - Animation library (Framer Motion)
- **Lucide React** - Beautiful icon library

## Quick Start

### Prerequisites
- Node.js 18+
- npm or yarn

### Installation & Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

The application will be available at `http://localhost:5174`

## Development Commands

```bash
# Development server with hot reload
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Run ESLint for code quality
npm run lint
```

## Project Structure

```
frontend/
├── src/
│   ├── main.tsx                   # App entry point with black background layout
│   ├── components/
│   │   ├── file-info-card.tsx     # File listing card with API integration
│   │   ├── anthropic-info-card.tsx # AI deletion suggestions display
│   │   ├── delete-button.tsx      # Red dangerous action button
│   │   ├── trash-button.tsx       # Yellow-orange caution button
│   │   └── ui/                    # Radix UI + shadcn/ui components
│   ├── services/api/
│   │   └── api.ts                 # Backend API client functions
│   ├── types/
│   │   └── api.ts                 # TypeScript interfaces for API responses
│   ├── hooks/
│   │   └── use-mobile.ts          # Mobile detection hook
│   ├── lib/
│   │   └── utils.ts               # Utility functions (cn, clsx)
│   └── index.css                  # Global styles and Tailwind imports
├── components.json                # shadcn/ui configuration
├── tailwind.config.js            # Tailwind CSS configuration
├── vite.config.js                # Vite build configuration
└── tsconfig.json                 # TypeScript configuration
```

## Component Architecture

### Core Components

**FileInfoCard** (`file-info-card.tsx`)
- Displays file listing from Downloads folder
- Interactive card with click-to-load functionality
- Shows file metadata: name, size, age
- Glassmorphism design with motion animations

**AnthropicInfoCard** (`anthropic-info-card.tsx`)
- Shows AI-powered deletion suggestions
- Integrates with Claude API for intelligent recommendations
- Loading states and error handling
- Displays suggested files in formatted list

**Action Buttons**
- `TrashButton`: Yellow-orange caution styling for trash operations
- `DeleteButton`: Red danger styling for permanent deletion
- Both support loading states and click handlers

### UI Components

Built on **Radix UI** primitives with **shadcn/ui** styling:
- Accordion, Alert Dialog, Avatar, Badge
- Button, Calendar, Card, Carousel, Chart
- Command, Context Menu, Dialog, Dropdown
- Form, Hover Card, Input, Label, Menu
- Navigation, Pagination, Popover, Progress
- Radio Group, Scroll Area, Select, Sheet
- Sidebar, Skeleton, Slider, Switch
- Table, Tabs, Textarea, Toggle, Tooltip

## Features

### File Management Interface
- **Visual File Display**: Cards showing file information with metadata
- **Interactive Loading**: Click-to-load file information
- **Real-time Updates**: Dynamic file listing with loading states
- **Responsive Design**: Mobile-first approach with responsive breakpoints

### AI-Powered Suggestions
- **Smart Recommendations**: AI analysis of files safe to delete
- **Visual Feedback**: Clear indication of suggested files
- **Action Integration**: Direct integration with trash/delete operations
- **Status Indicators**: Success/error feedback for operations

### Modern UI/UX
- **Glassmorphism Design**: Backdrop blur effects and transparent layers
- **Motion Animations**: Smooth hover effects and transitions
- **Dark Theme**: Black background with light accents
- **Accessibility**: Full keyboard navigation and screen reader support

## API Integration

### API Client (`services/api/api.ts`)

```typescript
// Fetch files from Downloads folder
export const fetchFiles = async (): Promise<FetchDownloadsResponse>

// Get AI deletion suggestions
export const fetchCandidates = async (): Promise<FetchDownloadsResponse>

// Move suggested files to trash
export const trashCandidates = async (): Promise<boolean>
```

### Environment Configuration
The app supports environment-based API configuration:
```bash
# .env.local
VITE_API_BASE_URL=http://localhost:8000
```

## Development

### Code Quality
- **ESLint**: Configured with TypeScript and React rules
- **Type Safety**: Full TypeScript coverage with strict mode
- **Import Organization**: Automatic import sorting and organization
- **Component Props**: Proper TypeScript interfaces for all components

### Styling Approach
- **Utility-First**: Tailwind CSS for rapid styling
- **Component Variants**: Class variance authority for component variations
- **Responsive Design**: Mobile-first responsive breakpoints
- **Consistent Spacing**: Standardized spacing and sizing scale

### State Management
- **Local State**: React useState for component-level state
- **API State**: Direct API calls with loading states
- **Error Handling**: Comprehensive error boundaries and user feedback

## Build & Deployment

### Production Build
```bash
npm run build
```

Builds the app for production to the `dist` folder with:
- Optimized bundle with tree shaking
- CSS purging for smaller file sizes
- TypeScript compilation and type checking
- Asset optimization and compression

### Environment Variables
- `VITE_API_BASE_URL`: Backend API URL (defaults to http://localhost:8000)

## Browser Support

- **Modern Browsers**: Chrome 90+, Firefox 88+, Safari 14+, Edge 90+
- **ES Modules**: Native ES module support required
- **CSS Features**: CSS Grid, Flexbox, Custom Properties

## Troubleshooting

### Development Issues
- **Port Conflicts**: Vite uses port 5174 by default
- **API Connection**: Ensure backend is running on correct port
- **Type Errors**: Check TypeScript interfaces match API responses

### Build Issues
- **Memory Errors**: Increase Node.js memory limit if needed
- **Import Errors**: Ensure all imports use correct file extensions
- **Path Resolution**: Check tsconfig.json path mapping configuration

### Performance
- **Bundle Size**: Use `npm run build` and analyze bundle with tools
- **Image Optimization**: Optimize images for web delivery
- **Code Splitting**: Vite handles automatic code splitting
