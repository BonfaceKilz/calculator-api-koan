;;; guix.scm ---

;; Copyright (C) 2021 Bonface Munyoki K. <me@bonfacemunyoki.com>

;; Author: Bonface Munyoki K. <me@bonfacemunyoki.com>

;; This program is free software; you can redistribute it and/or
;; modify it under the terms of the GNU General Public License
;; as published by the Free Software Foundation; either version 3
;; of the License, or (at your option) any later version.

;; This program is distributed in the hope that it will be useful,
;; but WITHOUT ANY WARRANTY; without even the implied warranty of
;; MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
;; GNU General Public License for more details.

;; You should have received a copy of the GNU General Public License
;; along with this program. If not, see <http://www.gnu.org/licenses/>.

;;; Commentary:

;;; Code:


(use-modules
 (srfi srfi-1)
 (srfi srfi-26)
 (ice-9 match)
 (ice-9 popen)
 (ice-9 rdelim)
 (gn packages python)
 (gn packages python-web)
 (gnu packages base)
 (gnu packages check)
 (gnu packages python-check)
 ((guix build utils) #:select (with-directory-excursion))
 (guix build-system python)
 (guix gexp)
 (guix git-download)
 (guix licenses)
 (guix packages))

(define %source-dir (dirname (current-filename)))

(define git-file?
  (let* ((pipe (with-directory-excursion %source-dir
                                         (open-pipe* OPEN_READ "git" "ls-files")))
         (files (let loop ((lines '()))
                  (match (read-line pipe)
                    ((? eof-object?)
                     (reverse lines))
                    (line
                     (loop (cons line lines))))))
         (status (close-pipe pipe)))
    (lambda (file stat)
      (match (stat:type stat)
        ('directory #t)
        ((or 'regular 'symlink)
         (any (cut string-suffix? <> file) files))
        (_ #f)))))

(package
  (name "genenetwork3.git")
  (version "0.0.1")
  (source (local-file %source-dir
                      #:recursive? #t
                      #:select? git-file?))
  (propagated-inputs `(("coreutils" ,coreutils)
                       ("python" ,python-wrapper)
                       ("python-flask" ,python-flask)
                       ("python-mypy" ,python-mypy)
                       ("python-pylint" ,python-pylint)))
  (build-system python-build-system)
  (home-page "https://github.com/genenetwork/genenetwork3")
  (synopsis "Retail Store Discounts")
  (description "Retail Store Discounts")
  (license agpl3+))
