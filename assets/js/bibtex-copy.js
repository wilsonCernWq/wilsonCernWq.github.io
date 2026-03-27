/**
 * BibTeX Copy to Clipboard Functionality
 * Integrates with Jekyll's syntax highlighting and Minimal Mistakes theme
 */
document.addEventListener('DOMContentLoaded', function() {
  // Find all BibTeX code blocks using Jekyll's highlighting structure
  const bibtexBlocks = document.querySelectorAll(
    '.language-bibtex.highlighter-rouge code, ' +
    'pre code.language-bibtex, pre code.language-bib, ' +
    'code.language-bibtex, code.language-bib, ' +
    'pre code[class*="bibtex"], pre code[class*="bib"]'
  );
  
  bibtexBlocks.forEach(function(codeBlock) {
    // Find the appropriate container element
    let container_element = codeBlock.closest('.highlighter-rouge') || 
                           codeBlock.closest('pre') || 
                           codeBlock;
    
    // Skip if already processed
    if (container_element.closest('.bibtex-container')) {
      return;
    }
    
    // Create container wrapper
    const container = document.createElement('div');
    container.className = 'bibtex-container';
    
    // Wrap the container element
    container_element.parentNode.insertBefore(container, container_element);
    container.appendChild(container_element);
    
    // Create copy button
    const copyBtn = document.createElement('button');
    copyBtn.className = 'bibtex-copy-btn';
    copyBtn.innerHTML = '<i class="fas fa-copy"></i>Copy BibTeX';
    copyBtn.setAttribute('data-clipboard-text', codeBlock.textContent.trim());
    copyBtn.setAttribute('aria-label', 'Copy BibTeX citation to clipboard');
    
    // Add button to container
    container.appendChild(copyBtn);
  });
  
  // Initialize clipboard.js
  const clipboard = new ClipboardJS('.bibtex-copy-btn');
  
  clipboard.on('success', function(e) {
    const btn = e.trigger;
    const originalText = btn.innerHTML;
    
    // Show success state
    btn.innerHTML = '<i class="fas fa-check"></i>Copied!';
    btn.classList.add('copied');
    
    // Reset after 2 seconds
    setTimeout(function() {
      btn.innerHTML = originalText;
      btn.classList.remove('copied');
    }, 2000);
    
    e.clearSelection();
  });
  
  clipboard.on('error', function(e) {
    const btn = e.trigger;
    const originalText = btn.innerHTML;
    
    // Show error state
    btn.innerHTML = '<i class="fas fa-exclamation-triangle"></i>Error';
    
    // Reset after 2 seconds
    setTimeout(function() {
      btn.innerHTML = originalText;
    }, 2000);
  });
});