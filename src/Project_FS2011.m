function Project_FS2011()
	% Lese Daten ein:
	load('../data/t.mat');
	load('../data/p.mat');
	load('../data/b.mat');
	load('../data/uh_b.mat');

	N_elements = length(t(:, 1));
	N_points = length(p(:, 1));
	N_edges = length(b(:, 1));
	N_bPoints = length(uh_b(:,1));

	% Helmholtz-Konstante:
	k = 13;

	K = sparse(N_points, N_points);
	M = sparse(N_points, N_points);
	rhs = zeros(N_points, 1);
	% Assemblierung der Steifigkeits- und Massenmatrix:
	for el = 1:N_elements
		[K_el M_el] = Element_Stiffness_Mass_Matrix(t, p, el);
		K(t(el, 1:3), t(el, 1:3)) = K(t(el, 1:3), t(el, 1:3)) + K_el;
		M(t(el, 1:3), t(el, 1:3)) = M(t(el, 1:3), t(el, 1:3)) + M_el;
	end
	
	% Assembliere die Randbedingungen:
	M_1D = 1/3*[2 1; 1 2];
	for edge = 1:N_edges
		x = p(b(edge, 1), :);
		y = p(b(edge, 2), :);
		len_el = sqrt(sum((x-y).^2));
		K(b(edge, 1:2), b(edge, 1:2)) = K(b(edge, 1:2), b(edge, 1:2)) - 1i * k *  0.5 * len_el * M_1D;
	end
	A = K - k^2 * M;

	z = [0.5; 0.5];
	[rhs grad_rhs] = Assemb_RHS(t, p, z(1), z(2));

	% Berechne B = C*A^{-1}:
	[L, U, P] = lu(A');
	B = zeros(N_bPoints, N_points);
	for i = 1:N_bPoints
		nr = uh_b(i,1);
		e_i = zeros(N_points,1);
		e_i(nr) = 1;
		%row_vec = (A'\e_i)';
		y = L\(P*e_i);
		row_vec = (U\y)';
		B(i,:) = row_vec;
	end

	
	nablaJ = real((grad_rhs' * B') * (B * rhs - uh_b(:,2)));

	% Steepest Descent Verfahren:
	alpha = 2;
	i = 0;
	fid = fopen('results/z.txt', 'w');
	fprintf('Iteration\tz\t\t\tNorm von grad(J(z))\n');
	fprintf('%d\t\t(%.4f, %.4f)\t%.2e\n', i, z(1), z(2), norm(nablaJ));
	fprintf(fid, '%.11f %.11f %.11f\n', z(1), z(2), norm(nablaJ));
	i = 1;
	while norm(nablaJ) >= 1e-6
		d = -nablaJ;
		z = z + alpha * d;
		[rhs grad_rhs] = Assemb_RHS(t, p, z(1), z(2));
		nablaJ = real((grad_rhs' * B') * (B * rhs - uh_b(:,2)));
		fprintf('%d\t\t(%.4f, %.4f)\t%.2e\n', i, z(1), z(2), norm(nablaJ));
		fprintf(fid, '%.11f %.11f %.11f\n', z(1), z(2), norm(nablaJ));
		i = i+1;
	end
	fclose(fid);

	fprintf('Position der Quelle: (%.3f, %.3f)\n', z(1), z(2));
	
	fid = fopen('results/u.txt', 'w');
	u = real(A\rhs);
	fprintf(fid, '%.11f\n', u);
	fclose(fid);
end
