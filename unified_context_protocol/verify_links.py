import os
import re
from pathlib import Path
from urllib.parse import unquote

def find_markdown_files(root_dir):
    for root, dirs, files in os.walk(root_dir):
        if 'node_modules' in dirs:
            dirs.remove('node_modules')
        if '.git' in dirs:
            dirs.remove('.git')
        for file in files:
            if file.endswith('.md'):
                yield Path(root) / file

def check_structure():
    root_dir = Path.cwd()
    print(f"Scanning for broken links in: {root_dir}")
    print("-" * 50)
    
    broken_links = []
    checked_count = 0
    
    # Regex for markdown links: [text](path)
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    
    for file_path in find_markdown_files(root_dir):
        try:
            content = file_path.read_text(encoding='utf-8')
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            continue
            
        matches = link_pattern.findall(content)
        
        for text, target in matches:
            # Skip external links and anchors
            if target.startswith('http') or target.startswith('#') or target.startswith('mailto:'):
                continue
            
            # Remove anchor part for file existence check
            target_file_part = target.split('#')[0]
            if not target_file_part:
                continue

            # Handle placeholders (simulate them as valid or skip)
            if "[CONTEXT_ROOT]" in target:
                continue # Cannot verify placeholders dynamically
                
            checked_count += 1
            
            # Resolve path
            # If starts with /, treated as relative to root (GitHub style often implies this, but standard md is relative)
            # We will assume standard relative paths unless it clearly looks like a root-relative path
            
            if target_file_part.startswith('/'):
               resolved_path = root_dir / target_file_part.lstrip('/')
            else:
               resolved_path = (file_path.parent / target_file_part).resolve()
            
            if not resolved_path.exists():
                broken_links.append({
                    'source': file_path.relative_to(root_dir),
                    'target': target,
                    'resolved': resolved_path
                })

    print(f"Checked {checked_count} internal links.")
    
    if broken_links:
        print(f"FOUND {len(broken_links)} BROKEN LINKS:")
        for link in broken_links:
            print(f"  File: {link['source']}")
            print(f"  Link: {link['target']}")
            print(f"  Err : Target not found")
            print("")
    else:
        print("✅ No broken static links found.")

if __name__ == "__main__":
    check_structure()
