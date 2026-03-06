#!/bin/bash
# Fully automated PDF conversion script
# This will install BasicTeX if needed and convert all files

echo "Automated PDF Converter for Board Documents"
echo "=========================================="

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check if BasicTeX is installed
if ! command_exists pdflatex; then
    echo "BasicTeX not found. Installing..."
    brew install --cask basictex
    
    # Add BasicTeX to PATH
    echo 'export PATH="/usr/local/texlive/2023basic/bin/universal-darwin:$PATH"' >> ~/.zshrc
    export PATH="/usr/local/texlive/2023basic/bin/universal-darwin:$PATH"
    
    # Also try the newer path structure
    export PATH="/Library/TeX/texbin:$PATH"
    
    echo "BasicTeX installed. You may need to restart your terminal after this script."
fi

# Update tlmgr and install required packages
echo "Updating LaTeX packages..."
sudo tlmgr update --self 2>/dev/null || true
sudo tlmgr install collection-fontsrecommended 2>/dev/null || true

# Get script directory and change to it
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Create PDFs directory
mkdir -p PDFs

# Find all markdown files in the Markdown Files directory
if [ -d "Markdown Files" ]; then
    echo "Found Markdown Files directory, converting all .md files..."
    # Use array to store files
    files=()
    while IFS= read -r -d '' file; do
        files+=("$file")
    done < <(find "Markdown Files" -name "*.md" -print0)
else
    echo "Markdown Files directory not found, looking for .md files in current directory..."
    # Fallback to current directory
    files=()
    while IFS= read -r -d '' file; do
        files+=("$file")
    done < <(find . -maxdepth 1 -name "*.md" -not -name "README*.md" -print0)
fi

converted=0
total=${#files[@]}

if [ $total -eq 0 ]; then
    echo "No markdown files found to convert."
    exit 1
fi

echo ""
echo "Converting files..."

for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        base_name=$(basename "$file" .md)
        output="PDFs/${base_name}.pdf"
        
        echo "Converting: $file"
        
        # Try pandoc with pdflatex
        if pandoc "$file" \
            -o "$output" \
            --pdf-engine=pdflatex \
            --variable geometry:margin=1in \
            --variable fontsize=11pt \
            --variable fontfamily=times \
            --table-of-contents=false \
            2>/dev/null; then
            echo "✓ Success: $output"
            ((converted++))
        else
            echo "  → Trying alternative engine..."
            # Try with xelatex if pdflatex fails
            if pandoc "$file" \
                -o "$output" \
                --pdf-engine=xelatex \
                --variable geometry:margin=1in \
                --variable fontsize=11pt \
                2>/dev/null; then
                echo "✓ Success: $output"
                ((converted++))
            else
                echo "✗ Failed: $file"
            fi
        fi
    else
        echo "✗ File not found: $file"
    fi
done

echo ""
echo "=========================================="
echo "Conversion Results: $converted/$total files converted"

if [ $converted -gt 0 ]; then
    echo ""
    echo "✓ PDF files ready in: PDFs/"
    echo "✓ Files can be attached to board meeting emails"
    echo ""
    ls -la PDFs/
else
    echo ""
    echo "✗ No files were converted."
    echo "  This might be due to LaTeX installation issues."
    echo "  Try running this script again or restart your terminal."
fi

echo ""
echo "Note: If you see permission errors, try:"
echo "sudo chown -R \$(whoami) /usr/local/texlive/"