# latexmk configuration: keep temporary files in build/
$aux_dir = 'build';
$out_dir = 'build';

# Create build directory if missing
$ensure_path = 1;

# Enable SyncTeX for forward/inverse search
$pdflatex = 'pdflatex -synctex=1 %O %S';

# Clean up auxiliary files with -c
$clean_ext = 'aux bbl blg fdb_latexmk fls log synctex.gz toc lof lot out nav snm';
